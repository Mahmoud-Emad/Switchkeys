import SwitchKeys from "./switchkeys/core/base";

async function main() {
  const switchkeys = new SwitchKeys();
  const user = await switchkeys.auth.register(
    {
      email:"Wa2el2@gmail.com",
      firstName: "3azzez",
      lastName: "Wab2s",
      password: "0000",
    }
  );
}

main();