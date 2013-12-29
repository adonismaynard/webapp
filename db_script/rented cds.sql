/*Display the rented CDs.*/
SELECT (tblcustomer.fname,  tblcustomer.mname, tblcustomer.lname) as rented_by, tblcdetail.movietitle as rented_cds
FROM tblcdonrent, tbltransaction, tblcdetail,tblcustomer
WHERE 	tbltransaction.cdcode=tblcdonrent.cdcode and
	tblcdonrent.cid=tblcustomer.cid and 
	tblcustomer.cid=tbltransaction.cid and 
	tbltransaction.cdcode=tblcdetail.cdcode and 
	tbltransaction.services='rent' and tbltransaction.petsa=tblcdonrent.petsa 