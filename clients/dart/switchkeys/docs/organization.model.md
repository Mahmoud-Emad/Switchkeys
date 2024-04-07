# SwitchKeys Organizations API Example

This Dart script demonstrates how to use the SwitchKeys organizations API. It includes operations such as creating, retrieving, updating, and deleting organizations. Error handling is also incorporated to manage any errors that may occur during these processes.

## Prerequisites

Before using this script, ensure that you have the SwitchKeys library installed and configured in your Dart project. Additionally, you must have valid credentials (email and password) for authentication with the SwitchKeys API.

## Usage

To use this script, follow these steps:

1. **Import Dependencies**: Import the required dependencies at the top of your Dart file.

   ```dart
   import 'package:switchkeys/src/api/response/types.dart';
   import 'package:switchkeys/src/core/base.dart';
   ```

2. **Define the Main Function**: Define the main function `organizationsMain()` for organization-related operations.

   ```dart
   void organizationsMain() async {
       // Code for organization operations goes here
   }
   ```

3. **Instantiate SwitchKeys**: Get an instance of SwitchKeys to interact with the SwitchKeys API.

   ```dart
   final SwitchKeys switchKeys = SwitchKeys();
   ```

4. **Authenticate User**: Log in the user using their email and password. This step is necessary if the saved token is expired.

   ```dart
   await switchKeys.auth.login(email: "email@example.com", password: "password");
   ```

5. **Organization Operations**: Perform various organization operations within a try-catch block to handle any potential errors.

   - **Create Organization**: Create a new organization with a unique name.

   - **Get Organization by Name**: Retrieve an existing organization by its name, as the name is unique for the user.

   - **Update Organization**: Update an existing organization with new data, such as name or members.

   - **Delete Organization**: Delete the organization.

   Example usage:

   ```dart
   try {
      organization = await switchKeys.organizations.getByName(organizationName: 'Cloud for students');
      print("Organization name: ${organization.name}");
   } catch (e) {
       // Error handling
   }
   ```

6. **Handle Errors**: In the catch block, handle any errors that may occur during organization operations.

   ```dart
   } catch (e) {
       print("Error occurred: $e");
   }
   ```

## Example

Here's how you can use the `organizationsMain()` function in your Dart code:

```dart
void main() {
    // Call the organizationsMain function to perform organization operations
    organizationsMain();
}
```

Replace `"email@example.com"` and `"password"` with your actual email and password for authentication with the SwitchKeys API.
