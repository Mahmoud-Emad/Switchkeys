// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys";

import SwitchKeys from "../src/core/base";

/**
 * `authExample` demonstrates the usage of authentication services.
 * This example guides users and developers on how to interact with the
 * SwitchKeys client for login and logout operations.
 */
export async function authExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // --------------------------------------------------------------------------------------------------------------------
  // Logging in to SwitchKeys
  // --------------------------------------------------------------------------------------------------------------------
  // First, log in to SwitchKeys with valid credentials.
  await switchkeys.auth.login({
    email: "admin@gmail.com",
    password: "0000",
  });

  console.log("Logged in successfully.");

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

  console.log("Logged out successfully.");
}
