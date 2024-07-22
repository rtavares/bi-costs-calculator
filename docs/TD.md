# Technical Description
The Technical Description document should describe the sequence of development steps that will lead to a product able to comply with the needs described on the Business Requirements.

In this case, we choose to take an unstructured approach, "running fast", "startup style".

In a proper setup project, each T.D. item would correspond to a repository branch.

## Branch management strategy:
- `main` - PROD, stable  branch.
- `development` - Staging / UAT
- `feature branches` QA

Once PythonAnywhere, that we are using to deployment, only supports one application on the free tier, we cannot run different instances of the project at the same time.   
We need to manually switch branches to do the testing.

The footer on the frontend page displays the branch on which the application is running.
 
--------


