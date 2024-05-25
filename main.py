import logging
from enum import Enum
from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException, Query
from pydantic import BaseModel

logger = logging.getLogger('di')
logging.basicConfig(level=logging.INFO)

class Deal(BaseModel):
    id: str
    title: str
    stage: str
    

class CRMManager:
    class InMemoryDB(BaseModel):
        deals: Dict[str, List[Deal]]

    def get_deals(self, customer_id: str) -> List[Deal]:
        raise NotImplementedError


class SalesforceManager(CRMManager):
    def __init__(self):
        self.db = CRMManager.InMemoryDB.parse_file('data/salesforce.json')

    def get_deals(self, customer_id: str) -> List[Deal]:
        logger.info(f"Fetching deals for customer '{customer_id}' from Salesforce")
        return self.db.deals.get(customer_id, [])
    
class HubspotManager(CRMManager):
    def __init__(self):
        self.db = CRMManager.InMemoryDB.parse_file('data/hubspot.json')

    def get_deals(self, customer_id: str) -> List[Deal]:
        logger.info(f"Fetching deals for customer '{customer_id}' from Hubspot")
        return self.db.deals.get(customer_id, [])


class CRMEnum(str, Enum):
    salesforce='salesforce'
    hubspot='hubspot'

CRM_MAPPING = {
    CRMEnum.hubspot: HubspotManager,
    CRMEnum.salesforce: SalesforceManager
}


class Customer(BaseModel):
    id: str
    name: str
    crm: CRMEnum


# Actual Application
app = FastAPI()

def get_customer(customer_id: str = Query(...)) -> Customer:
    mocked_db = {
        'customer_a': Customer(id='customer_a', name='Apricot', crm=CRMEnum.salesforce),
        'customer_b': Customer(id='customer_b', name='Barrel', crm=CRMEnum.hubspot),
    }

    if customer_id not in mocked_db:
        raise HTTPException(404, detail='Customer not found')
    return mocked_db[customer_id]

def get_crm_manager(customer: Customer = Depends(get_customer)) -> CRMManager:
    if customer.crm not in CRM_MAPPING:
        raise HTTPException(404, detail='CRM not supported')
    logger.info(f"Creating CRM Manager: {customer.crm}")
    return CRM_MAPPING[customer.crm]()


class DealResponse(BaseModel):
    crm_provider: CRMEnum
    deals: List[Deal]

@app.get("/deals")
def list_deals(customer= Depends(get_customer), crm_manager= Depends(get_crm_manager)) -> DealResponse:
    return DealResponse(crm_provider=customer.crm, deals=crm_manager.get_deals(customer.id))
