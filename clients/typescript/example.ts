import SwitchKeys from "./switchkeys/core/base";

async function main() {
  const switchkeys = new SwitchKeys();
  const user = await switchkeys.auth.register(
    {
      email:"Wa2el222@gmail.com",
      firstName: "3azzez",
      lastName: "Wab2s",
      password: "0000",
    }
  );

  // const user = await switchkeys.auth.login({
  //   email: "",
  //   password: ""
  // });

}

main();