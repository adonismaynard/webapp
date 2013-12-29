SELECT tblcdetail.cdcode,
       tblcdetail.movietitle as rented_cds,
       tblcat.genre
                 FROM 
                 tblcdetail,
                 tblcat
                 WHERE 
                 tblcdetail.gencode=tblcat.gencode
