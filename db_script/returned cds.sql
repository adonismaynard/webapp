/*Display the returned CDs.*/
SELECT tblcdetail.movietitle as returned_cds, tblcustomer.fname,  tblcustomer.mname, tblcustomer.lname,tbltransaction.petsa as Date_Returned
FROM tblcdreturned, tbltransaction, tblcdetail, tblcustomer
WHERE tblcdreturned.cid=tblcustomer.cid and tblcustomer.cid=tbltransaction.cid and tblcdreturned.cdcode=tbltransaction.cdcode and tbltransaction.cdcode=tblcdetail.cdcode and tbltransaction.services='returned'