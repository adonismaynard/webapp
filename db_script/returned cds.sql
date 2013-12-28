/*Display the returned CDs.*/
SELECT (tblcustomer.fname,  tblcustomer.mname, tblcustomer.lname) as rented_by, tblcdetail.movietitle as returned_cds
FROM tblcdreturned, tbltransaction, tblcdetail, tblcustomer
WHERE tblcdreturned.cid=tblcustomer.cid and tblcustomer.cid=tbltransaction.cid and tblcdreturned.cdcode=tbltransaction.cdcode and tbltransaction.cdcode=tblcdetail.cdcode and tbltransaction.services='returned'