add-cash:
	python nwFIRE.py --portfolio KYLE add cash

add-fund:
	python nwFIRE.py --portfolio KYLE add fund

delete-fund:
	python nwFIRE.py --portfolio TEST delete KEY 

edit-cash:
	python nwFIRE.py --portfolio KYLE edit CASH --field amount --value 500

summary:
	python nwFIRE.py --portfolio JOINT summary

summary-asset:
	python nwFIRE.py --portfolio JOINT summary --asset VWSTX

report:
	python nwFIRE.py --portfolio JOINT report

