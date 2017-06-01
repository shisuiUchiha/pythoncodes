import re

x="From santhukota1996@gmail.com s@t"

y=re.findall('^From \S+@(\S+)',x);

z=x.split();

z=z[1].split('@');

print z[1];


print y;
