import 'package:switchkeys/src/api/models/auth.dart';
import 'package:switchkeys/src/api/models/organizations.dart';
import 'package:switchkeys/src/api/models/projects.dart';
import 'package:switchkeys/src/api/models/environments.dart';
import 'package:switchkeys/src/api/models/users.dart';

class SwitchKeys {
  SwitchKeys();

  SwitchKeyAuth auth = SwitchKeyAuth();
  SwitchKeysOrganizations organizations = SwitchKeysOrganizations();
  SwitchKeysProjects projects = SwitchKeysProjects();
  SwitchKeysEnvironments environments = SwitchKeysEnvironments();
  SwitchKeysUsers users = SwitchKeysUsers();
}
