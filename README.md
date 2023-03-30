# click-automation-windows-python-coordenation
Codigo simples criado em python que você usa comandos de cmd para clicar nas coordenadas passadas exe: <br>
<b> Node.js </b><br>
```
const {
    exec
  } = require('child_process');
  
  
  
  
  
  
  function cmd(comandoDeCmd = "tree") {
    exec(comandoDeCmd, (err, stdout, stderr) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(stdout);
    });
  }

  
  cmd('click.py 1000 700')
```
