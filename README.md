# pathTrasverser

<p>A python tool that tests path trasversal vulnerability.</p>

## How it works ?

<p>Upon running the tool you'll be prompted to enter a link<br>
to the website do not forget the slash (/) at the end of the <br>
link.Next you'll have to enter a payload for example ../../../../etc.<br>
The tool will run the payload against the link given.It will also try<br>
some filter evasion techniques as for now only single and double URL <br>
encoding and unicode encoding are supported</p>

## References 
<a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md">PayloadsAllTheThings</a>

## Requirements
<ol>
  <li>Python</li>
</ol>

## Installation

```
git clone https://github.com/peterhinga/pathTrasverser

cd pathTrasverser

pip3 install pyfiglet, urllib3, requests

python3 main.py
```

## Contributions
All contributions are welcome.
