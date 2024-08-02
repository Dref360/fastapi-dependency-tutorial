## Real-life example of Dependency Injection using FastAPI

Author: Frederic Branchaud-Charron (@Dref360)

**Goal**: Provide an real-world example of a dependency injection setup.

In this tutorial, we will visit a usecase often seen in production. Your customers probably store their data in different systems which makes it hard for your system to know where to look.


Our App will use Dependency Injection to fetch our customers' deals from multiple CRM (Salesforce or Hubspot).

<a href="https://www.youtube.com/watch?v=47pLaFosHRE">
  <img src="https://github.com/Dref360/fastapi-dependency-tutorial/assets/8976546/0ac52c33-50cc-4456-9c33-ebb7a5ee7f36" width="40%" />
</a>


**Resources**

- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/)
- [FastAPI Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Dependency Injection (Wiki)](https://en.wikipedia.org/wiki/Dependency_injection)
- [Stackify](https://stackify.com/dependency-injection/)


**Dependency Injection** (DI) is a Design Pattern well used in Industry and in particular in "Enterprise Languages" such as Java or C#. 

The objective of using DI is to make a class independent of its dependencies.[SOLID principles]() are easily followed when using this pattern.

DI has many advantages:
* Dependencies are reusable.
* Dependencies can be mocked, allowing easier testing of a class.



**Why this tutorial?**

The most common example of DI is the "Logger" example which I find uninspiring and doesn't teach you why you should use DI. I wanted to propose a practical example that anyone can easily understand.
