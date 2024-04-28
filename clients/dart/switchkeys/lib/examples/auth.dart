// This Dart script demonstrates how to use the SwitchKeys authentication API.
// It first logs in an existing user with the provided email and password,
// handling any errors that may occur during the login process.
// Then, it registers a new user with the specified details,
// such as first name, last name, email, password, and user type.
// Again, error handling is included to manage any errors that may occur during the registration process.

import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

void authMain() async {
  // Get an instance of SwitchKeyAuth
  SwitchKeys switchKeys = SwitchKeys();

  // Now you can use the auth instance to make API calls
  // Logging in an existing user
  await switchKeys.auth
      .login(email: "", password: "")
      .then((user) => print("Logged in successfully: ${user.email}"))
      .catchError((e) => print("Error logging in: $e"));

  // Registering a new user
  await switchKeys.auth
      .register(
        firstName: "Ahmed",
        lastName: "Zain",
        email: "",
        password: "",
        memberType: UserTypeEnum.administrator,
      )
      .then((user) => print("User registered successfully: ${user.email}"))
      .catchError((e) => print("Error registering user: $e"));
}
