// This example demonstrates the usage of the SwitchKeys TS Client to interact with the SwitchKeys system.

// First, import the SwitchKeys class.
import SwitchKeys from "./switchkeys/core/base";

/**
 * Main function to demonstrate SwitchKeys usage.
 */
async function main() {
  // Create an instance of the SwitchKeys class.
  const switchkeys = new SwitchKeys();

  // If it's the first time using SwitchKeys and no member has been created yet, register a new member.
  // PS: This will also generate and save member tokens into the `config.ini` file.
  // Uncomment the following code and replace placeholders with actual member data.
  /*
  const newMember = await switchkeys.auth.register({
    email: "<member_email>",
    firstName: "<member_first_name>",
    lastName: "<member_last_name>",
    password: "<password>",
  });
  console.log(`New member registered. Access token: ${newMember.accessToken}`);
  */

  // If a member has already been created, login using their email and password to generate and save tokens in the `config.ini` file.
  // Uncomment the following code and replace placeholders with actual member credentials.
  /*
  const loggedInMember = await switchkeys.auth.login({
    email: "<member_email>",
    password: "<password>",
  });
  console.log(`Member logged in. Access token: ${loggedInMember.accessToken}`);
  */

  // If a member has been created and you know their ID, retrieve their data using the `getByID` method under the `organizations.members` module.
  // Uncomment the following code and replace the ID placeholder with the actual member ID.
  /*
  const memberId = 9; // Replace with the actual member ID
  const memberByID = await switchkeys.organizations.members.getByID(memberId);
  console.log(`Member data retrieved by ID. First name: ${memberByID.firstName}`);
  */

  // If you have a member created and you know their email, retrieve their data using the `getByEmail` method under the `organizations.members` module.
  // Uncomment the following code and replace the email placeholder with the actual member email.
  /*
 const memberEmail = "john@example.com"; // Replace with the actual member email
 const memberByEmail = await switchkeys.organizations.members.getByEmail(memberEmail)
 console.log(`Member data retrieved by email. First name: ${memberByEmail.firstName}`);
 */

  // If you have a member created and you know their ID, update their data using the `update` method under the `organizations.members` module.
  // Uncomment the following code and replace the memberId placeholder with the actual member ID.

  // Use the login method to update the user tokens.
  await switchkeys.auth.login({ email: "admin@gmail.com", password: "0000" });

  const memberId = 9; // Replace with the actual member ID
  // Get the member first to check the first name.
  const member = await switchkeys.organizations.members.getByID(memberId);
  // Print it out
  console.log(`Member data retrieved by ID. First name: ${member.firstName}`); // Mahmoud
  
  // Create an organization
  const organization = await switchkeys.organizations.create({ name: "Test" });
  console.log(`Member organization ID: ${organization.id}`);
}

// Call the main function to execute the example.
main();
