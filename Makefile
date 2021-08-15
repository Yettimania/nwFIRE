add-cash:
	python nwFIRE.py --portfolio KYLE add cash

add-fund:
	python nwFIRE.py --portfolio KYLE add fund

delete-fund:
	python nwFIRE.py --portfolio TEST delete KEY 

edit-cash:
	python nwFIRE.py --portfolio KYLE edit CASH --field amount --value 500
