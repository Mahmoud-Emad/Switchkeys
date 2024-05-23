// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys";

import SwitchKeys from "../src/core/base";
import { SwitchKeysUserType } from "../src/utils/types";

/**
 * `authExample` demonstrates the usage of authentication services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys client for login and logout operations.
 */
export async function authExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();
  const userEmail = "testing@switchkeys.com";

  // --------------------------------------------------------------------------------------------------------------------
  // Check if the user is already created
  // --------------------------------------------------------------------------------------------------------------------
  console.log(`[+] Check if user with email ${userEmail} is registered.`);
  const userCreated = await switchkeys.users.isUserCreated({
    email: userEmail,
  });

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  if (!userCreated) {
    // If you haven't created account yet, unlock the register method.
    await switchkeys.auth.register({
      email: userEmail,
      password: "0000",
      firstName: "Testing",
      lastName: "Account",
      memberType: SwitchKeysUserType.Administrator,
    });
    console.log("[+] Registered successfully.");
  } else {
    console.log(`[!] User with email ${userEmail} is already registered.`);
    await switchkeys.auth.login({
      email: userEmail,
      password: "0000",
    });
    console.log("[+] Logged in successfully.");

    // --------------------------------------------------------------------------------------------------------------------
    // Demonstrate other authenticated operations here
    // --------------------------------------------------------------------------------------------------------------------
    // For example, you can now perform operations that require authentication, such as accessing user data,
    // loading environments, or managing projects and organizations.

    // --------------------------------------------------------------------------------------------------------------------
    // Logging out of SwitchKeys
    // --------------------------------------------------------------------------------------------------------------------
    // Finally, log out of SwitchKeys.
    switchkeys.auth.logout();
    console.log("[+] Logged out successfully.");
  }
}
