SELECT tblcustomer.cid,tblcdonrent.petsa,
                 tblcdetail.movietitle as rented_cds,
		 tbltransaction.borroweddisc, 
		 tblcustomer.fname,tblcustomer.mname, tblcustomer.lname
                 FROM tblcdonrent,
                 tbltransaction,
                 tblcdetail,
                 tblcustomer,
                 tblcat
                 WHERE tblcdonrent.cid=tblcustomer.cid and
                 tblcustomer.cid=tbltransaction.cid
                 and tblcdonrent.cdcode=tbltransaction.cdcode and
                 tbltransaction.cdcode=tblcdetail.cdcode and
                 tbltransaction.services='rent' and
                 tbltransaction.petsa=tblcdonrent.petsa
                 and tblcdetail.gencode=tblcat.gencode
