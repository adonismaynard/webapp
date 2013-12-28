/*display all the cd*/
SELECT movietitle, genre

FROM tblcdetail cd, tblcat cat

WHERE cd.gencode=cat.gencode