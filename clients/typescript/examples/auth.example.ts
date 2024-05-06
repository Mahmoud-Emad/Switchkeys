// Import the SwitchKeys class from the client library.
// import SwitchKeys from "switchkeys";
import SwitchKeys from "../switchkeys/core/base";

/**
 * Main function demonstrating the usage of the SwitchKeys client.
 */
export async function authExample() {
  // Create an instance of the SwitchKeys client.
  const switchkeys = new SwitchKeys();

  // Uncomment and replace placeholders with actual data to register a new member.
  /*
  const newMember = await switchkeys.auth.register({
    email: "<member_email>",
    firstName: "<member_first_name>",
    lastName: "<member_last_name>",
    password: "<password>",
  });
  console.log(`New member registered. Access token: ${newMember.accessToken}`);
  */

  // Uncomment and replace placeholders with actual credentials to log in an existing member.
  /*
  const loggedInMember = await switchkeys.auth.login({
    email: "<member_email>",
    password: "<password>",
  });
  console.log(`Member logged in. Access token: ${loggedInMember.accessToken}`);
  */
}
