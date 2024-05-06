// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys-ts-client";
import SwitchKeys from "../switchkeys/core/base";

/**
 * Main function demonstrating the usage of the SwitchKeys client.
 */
export async function organizationExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // Uncomment and replace the ID placeholder with the actual member ID to retrieve member data by ID.
  /*
  const memberId = 9; // Replace with the actual member ID
  const memberByID = await switchkeys.organizations.members.getById(memberId);
  console.log(`Member data retrieved by ID. First name: ${memberByID.firstName}`);
  */

  // Uncomment and replace the email placeholder with the actual member email to retrieve member data by email.
  /*
  const memberEmail = "john@example.com"; // Replace with the actual member email
  const memberByEmail = await switchkeys.organizations.members.getByEmail(memberEmail);
  console.log(`Member data retrieved by email. First name: ${memberByEmail.firstName}`);
  */

  // Uncomment and replace the memberId placeholder with the actual member ID to update member data.
  // Use the login method before updating the user tokens.
  /*
  await switchkeys.auth.login({ email: "admin@gmail.com", password: "0000" });
  const memberId = 9; // Replace with the actual member ID
  const member = await switchkeys.organizations.members.getById(memberId);
  console.log(`Member data retrieved by ID. First name: ${member.firstName}`);
  */

  // Uncomment and replace the data placeholder with actual organization data to create a new organization.
  /*
  const organization = await switchkeys.organizations.create({ name: "Test" });
  console.log(`Organization ID: ${organization.id}`);
  */

  // Uncomment and replace the organization ID placeholder with the actual ID to get organization data by ID.
  /*
  const organization = await switchkeys.organizations.getById(5);
  console.log(`Organization name: ${organization.name}`);
  */

  // Uncomment and replace the organization ID placeholder with the actual ID to delete an organization.
  /*
  await switchkeys.organizations.delete(5); // Returns null or error
  */

 let organization = await switchkeys.organizations.getById(6);
 console.log(`Organization name: ${organization.name}`);
//  organization = await switchkeys.organizations.update(6, { name: "Test 2" });
//  console.log(`Organization name: ${organization.name}`);
}
