// This Dart script demonstrates how to use the SwitchKeys authentication API.

import 'package:switchkeys/src/api/response/types.dart';
import 'package:switchkeys/src/core/base.dart';

/// `authExample` demonstrates the usage of authentication services.
/// This example guides users and developers on how to interact with the
/// SwitchKeys client for login and logout operations.
Future<void> authExample() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchkeys = SwitchKeys();

  print('\n------------------------------------------------------------------');
  print('### Running the auth example ###');
  print('------------------------------------------------------------------\n');

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  try {
    // If you haven't created account yet, unlock the register method.
    var user = await switchkeys.auth.register(
      firstName: "Testing",
      lastName: "Account",
      email: "testing@switchkeys.com",
      password: "0000",
      memberType: UserTypeEnum.administrator,
    );
    print("[+] Registered successfully: ${user.email}");
  } catch (e) {
    var user = await switchkeys.auth.login(
      email: "testing@switchkeys.com",
      password: "0000",
    );
    print("[+] Logged in successfully: ${user.email}");

    // --------------------------------------------------------------------------------------------------------------------
    // Demonstrate other authenticated operations here
    // --------------------------------------------------------------------------------------------------------------------
    // For example, you can now perform operations that require authentication, such as accessing user data,
    // loading environments, or managing projects and organizations.
  } finally {
    // --------------------------------------------------------------------------------------------------------------------
    // Logging out of SwitchKeys
    // --------------------------------------------------------------------------------------------------------------------
    // Finally, log out of SwitchKeys.
    switchkeys.auth.logout();
    print("[+] Logged out successfully");
  }
}
