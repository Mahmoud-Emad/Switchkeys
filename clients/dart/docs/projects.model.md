# SwitchKeys Projects API Example

This Dart script demonstrates how to use the SwitchKeys projects API. It includes operations such as creating, retrieving, updating, and deleting projects. Error handling is also incorporated to manage any errors that may occur during these processes.

## Prerequisites

Before using this script, ensure that you have the SwitchKeys library installed and configured in your Dart project. Additionally, you must have valid credentials (email and password) for authentication with the SwitchKeys API.

## Usage

To use this script, follow these steps:

1. **Import Dependencies**: Import the required dependencies at the top of your Dart file.

   ```dart
   import 'package:switchkeys/src/api/response/types.dart';
   import 'package:switchkeys/src/core/base.dart';
   ```

2. **Define the Main Function**: Define the main function `projectsMain()` for project-related operations.

   ```dart
   void projectsMain() async {
       // Code for project operations goes here
   }
   ```

3. **Instantiate SwitchKeys**: Get an instance of SwitchKeys to interact with the SwitchKeys API.

   ```dart
   final SwitchKeys switchKeys = SwitchKeys();
   ```

4. **Authenticate User**: Log in the user using their email and password. This step is necessary if the saved token is expired.

   ```dart
   await switchKeys.auth.login(email: "email@example.com", password: "0000");
   ```

5. **Project Operations**: Perform various project operations within a try-catch block to handle any potential errors.

   - **Get Organization**: Retrieve the organization where the project will be created or updated.

   - **Create Project**: Create a new project under the retrieved organization.

   - **Get Project by ID**: Get an existing project by its ID.

   - **Update Project**: Update an existing project with new data, such as name or organization.

   - **Delete Project**: Delete the project.

   Example usage:

   ```dart
   try {
      final SwitchKeysProjectResponse project =
        await switchKeys.projects.getByID(projectID: 2);
    print("Project name: ${project.name}");
   } catch (e) {
       // Error handling
   }
   ```

6. **Handle Errors**: In the catch block, handle any errors that may occur during project operations.

   ```dart
   } catch (e) {
       print("Error occurred: $e");
   }
   ```

## Example

Here's how you can use the `projectsMain()` function in your Dart code:

```dart
void main() {
    // Call the projectsMain function to perform project operations
    projectsMain();
}
```

Replace `"email@example.com"` and `"password"` with your actual email and password for authentication with the SwitchKeys API.
