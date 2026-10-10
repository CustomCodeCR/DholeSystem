# Maersk — cambio manual de perfil Chromium, misma base PostgreSQL

Esta herramienta prepara una nueva sesión de Chromium en el MISMO entorno, sin cambiar el origen de PostgreSQL, identidades ni IP.

Dry-run: sudo bash /home/Argos/scripts/prepare-maersk-session.sh production --dry-run
Aplicar: sudo bash /home/Argos/scripts/prepare-maersk-session.sh production --apply REPLACE_CHROMIUM_SESSION

Se exige cero ejecuciones activas (consulta SQL de solo lectura). El script detiene de manera controlada solo los Agent Workers del entorno, renombra el perfil existente a un respaldo en el mismo volumen, crea uno nuevo con los mismos permisos y vuelve a iniciar el mismo contenedor. No borra datos ni reinicia bases de datos.

Requiere autenticación legítima en la sesión nueva. No soluciona CAPTCHA automáticamente, no cambia la identidad ni reintenta las ejecuciones pendientes. Un nuevo perfil no garantiza que Maersk deje de requerir verificación.

Antes de ejecutar --apply, revisar el dry-run y confirmar que no hay ejecuciones Running. El modo dry-run no escribe nada.