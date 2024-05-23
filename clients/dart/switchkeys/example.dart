import 'package:switchkeys/examples/auth.dart';
import 'package:switchkeys/examples/organization.dart';
import 'package:switchkeys/examples/projects.dart';
// import 'package:switchkeys/examples/environments.dart';

// import 'package:switchkeys/examples/full_example.dart';

main() async {
  await authExample();
  await organizationsMain();
  await projectsMain();

  // environmentsMain();
  // switchKeysFullExample();
  // switchKeysManagement();
}
