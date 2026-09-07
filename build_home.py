# -*- coding: utf-8 -*-
# Renders the Barboursville homepage from templates/home.html using the shared components.
exec(open("common.py").read())
s=open("templates/home.html",encoding="utf-8").read()
for k,v in {"{{NAV}}":NAV,"{{FOOTER}}":FOOTER,"{{STICKY}}":STICKY_BAR,"{{STATS}}":STATS_BRANDS,"{{PMATCH}}":PRICE_MATCH_BAND,"{{CONSULT}}":CONSULT_SECTION,"{{FINANCE}}":FINANCE_BAND,"{{BOOK}}":BOOK}.items():
    s=s.replace(k,v)
open("bundle/site/index.html","w",encoding="utf-8").write(s)
print("home: wrote index.html (%d bytes)"%len(s))
