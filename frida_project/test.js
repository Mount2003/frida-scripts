'use strict';

const target_mod = Process.enumerateModules().find(module => module.name.toLowerCase() === TARGET_PROC)
const target_imps = Module.enumerateImports(target_mod.name)
for (const imp of target_imps) {
	console.log(imp)
	Interceptor.attach(imp.address, {
		onEnter: function(args) {
			// for (const arg of args) {
				// send(`	${arg}`)
			// }
			send(`Testing`)
		} 
	})
}
