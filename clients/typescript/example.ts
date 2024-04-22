// This example demonstrates the usage of the SwitchKeys TS Client to interact with the SwitchKeys system.

// First, import the SwitchKeys class.
import SwitchKeys from "switchkeys-ts-client";

/**
 * Main function to demonstrate SwitchKeys usage.
 */
async function main() {
  const switchkeys = new SwitchKeys();

  // Register a new member if it's the first time using SwitchKeys and no member has been created yet.
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

  // Log in an existing member using their email and password to generate and save tokens in the `config.ini` file.
  // Uncomment the following code and replace placeholders with actual member credentials.
  /*
  const loggedInMember = await switchkeys.auth.login({
    email: "<member_email>",
    password: "<password>",
  });
  console.log(`Member logged in. Access token: ${loggedInMember.accessToken}`);
  */

  // Retrieve a member's data by their ID using the `getById` method under the `organizations.members` module.
  // Uncomment the following code and replace the ID placeholder with the actual member ID.
  /*
  const memberId = 9; // Replace with the actual member ID
  const memberByID = await switchkeys.organizations.members.getById(memberId);
  console.log(`Member data retrieved by ID. First name: ${memberByID.firstName}`);
  */

  // Retrieve a member's data by their email using the `getByEmail` method under the `organizations.members` module.
  // Uncomment the following code and replace the email placeholder with the actual member email.
  /*
 const memberEmail = "john@example.com"; // Replace with the actual member email
 const memberByEmail = await switchkeys.organizations.members.getByEmail(memberEmail)
 console.log(`Member data retrieved by email. First name: ${memberByEmail.firstName}`);
 */

  // Update a member's data using the `update` method under the `organizations.members` module.
  // Uncomment the following code and replace the memberId placeholder with the actual member ID.

  // Use the login method to update the user tokens.
  // await switchkeys.auth.login({ email: "admin@gmail.com", password: "0000" });

  // const memberId = 9; // Replace with the actual member ID
  // Get the member first to check the first name.
  // const member = await switchkeys.organizations.members.getById(memberId);
  // Print it out
  // console.log(`Member data retrieved by ID. First name: ${member.firstName}`); // Mahmoud

  // Create an organization
  // Uncomment the following code and replace the data placeholder with the actual organization data.
  /** 
   const organization = await switchkeys.organizations.create({ name: "Test" });
   console.log(`Organization ID: ${organization.id}`);
   */

  // after creating an organization, also, if you have an already created organization, you can get it's data by accessing the `getById` method.
  // Uncomment the following code and replace the data placeholder with the actual organization data.
  /**
   const organization = await switchkeys.organizations.getById(5);
   console.log(`Organization name: ${organization.name}`);
   */

  // Can delete an organization by accessing the `delete` method.
  // Uncomment the following code and replace the data placeholder with the actual organization data.
  /**
   await switchkeys.organizations.delete(5); // Returns null or error
   */

  // Can update by accessing the `update` method
  // Get the organization first to print it's data

  let organization = await switchkeys.organizations.getById(6);
  console.log(`Organization name: ${organization.name}`);

  // Then update it's name

  // organization = await switchkeys.organizations.update(6, {name: "Test 2"});
  // console.log(`Organization name: ${organization.name}`);

  // Adding members into it
  console.log(`Organization members: ${organization.members}`);
  organization = await switchkeys.organizations.addMember(organization.id, {memberId: 4});
  console.log(`Organization members: ${organization.members}`);
  // Removing the added member
  organization = await switchkeys.organizations.removeMember(organization.id, {memberId: 4});
  console.log(`Organization members: ${organization.members}`);
}

// Call the main function to execute the example.
main();
