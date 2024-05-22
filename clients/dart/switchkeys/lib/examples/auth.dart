// This Dart script demonstrates how to use the SwitchKeys authentication API.
// It first, it registers a new user with the specified details,
// Then logs in an existing user with the provided email and password,
// handling any errors that may occur during the login process.
// such as first name, last name, email, password, and user type.
// Again, error handling is included to manage any errors that may occur during the registration process.

// import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// `authExample` demonstrates the usage of authentication services.
/// This example guides users and developers on how to interact with the
/// SwitchKeys client for login and logout operations.
void authExample() async {
  // Create an instance of the SwitchKeys client.
  SwitchKeys switchKeys = SwitchKeys();
  // Now you can use the auth instance to make API calls
  // Logging in an existing user
  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  // If you haven't created account yet, unlock the register method.
  /**
  await switchKeys.auth
    .register(
      firstName: "Testing",
      lastName: "Account",
      email: "testing@switchkeys.com",
      password: "0000",
      memberType: UserTypeEnum.administrator,
    )
    .then(
      (user) => print("User registered successfully: ${user.email}"),
    )
    .catchError(
      (e) => print("Error registering user: $e"),
    );
  */

  // Registering a new user
  await switchKeys.auth
      .login(
        email: "testing@switchkeys.com",
        password: "0000",
      )
      .then(
        (user) => print("Logged in successfully: ${user.email}"),
      )
      .catchError(
        (e) => print("Error logging in: $e"),
      );

  // --------------------------------------------------------------------------------------------------------------------
  // Demonstrate other authenticated operations here
  // --------------------------------------------------------------------------------------------------------------------
  // For example, you can now perform operations that require authentication, such as accessing user data,
  // loading environments, or managing projects and organizations.

  // --------------------------------------------------------------------------------------------------------------------
  // Logging out of SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // Finally, log out of SwitchKeys.
  // switchkeys.auth.logout();
}
