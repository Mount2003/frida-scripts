'use strict';

const module_arr = Array.from(Process.enumerateModules())
const target_app_imports = Array.from(module_arr[0].enumerateImports())
send(target_app_imports)