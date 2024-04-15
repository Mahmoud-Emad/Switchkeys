// This example demonstrates the usage of the SwitchKeys TS Client to interact with the SwitchKeys system.

// First, import the SwitchKeys class.
import SwitchKeys from "./switchkeys/core/base";

/**
 * Main function to demonstrate SwitchKeys usage.
 */
async function main() {
  // Create an instance of the SwitchKeys class.
  const switchkeys = new SwitchKeys();

  // If it's the first time using SwitchKeys and no user has been created yet, register a new user.
  // PS: This will also generate and save user tokens into the `config.ini` file.
  // Uncomment the following code and replace placeholders with actual user data.
  /*
  const newUser = await switchkeys.auth.register({
    email: "<user_email>",
    firstName: "<user_first_name>",
    lastName: "<user_last_name>",
    password: "<password>",
  });
  console.log(`New user registered. Access token: ${newUser.accessToken}`);
  */

  // If a user has already been created, login using their email and password to generate and save tokens in the `config.ini` file.
  // Uncomment the following code and replace placeholders with actual user credentials.
  /*
  const loggedInUser = await switchkeys.auth.login({
    email: "<user_email>",
    password: "<password>",
  });
  console.log(`User logged in. Access token: ${loggedInUser.accessToken}`);
  */

  // If a user has been created and you know their ID, retrieve their data using the `getByID` method under the `users` module.
  // Uncomment the following code and replace the ID placeholder with the actual user ID.
  /*
  const userId = 9; // Replace with the actual user ID
  const userByID = await switchkeys.users.getByID(userId);
  console.log(`User data retrieved by ID. First name: ${userByID.firstName}`);
  */

  // If you have a user created and you know their email, retrieve their data using the `getByEmail` method under the `users` module.
  // Uncomment the following code and replace the email placeholder with the actual user email.
  const userEmail = "admin@gmail.coms"; // Replace with the actual user email
  const userByEmail = await switchkeys.users.getByEmail(userEmail)
  console.log(`User data retrieved by email. First name: ${userByEmail.firstName}`);
  /*
  */
}

// Call the main function to execute the example.
main();
