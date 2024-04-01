import 'package:switchkeys/src/api/models/auth.dart';

class SwitchKeys {
  static SwitchKeyAuth auth(String apiKey) => SwitchKeyAuth(apiKey: apiKey);
}

void main() async {
  // Provide your API key here
  String apiKey = "your_api_key";

  // Get an instance of SwitchKeyAuth
  SwitchKeyAuth auth = SwitchKeys.auth(apiKey);

  // Now you can use the auth instance to make API calls
  var user = await auth.login(email: "admin@gmail.com", password: "0000");
  print("user: ");
  print(user.email);
}
