﻿
drop table tblCDreturned;
drop table tblCDonRent;
drop table tbltransaction;
drop table tblcustomertransaction;
drop table tblcustomer;
drop table tblCDetail;
drop table tblCat;


create table tblCat(gencode serial not null, 
genre text not null,
unique (genre), 
primary key (gencode));

create table tblCDetail(cdCode serial not null, 
MovieTitle text not null, 
gencode serial not null, 
copyright dec(4) not null,
availability int not null,
Petsa date not null,
RentFee money not null, 
Primary key (cdCode),
Unique (MovieTitle),
foreign key (gencode) references tblCat(gencode));

create table tblcustomer(
cid serial not null,
fname text not null,
mname text null,
lname text not null,
Street text not null,
Purok text not null,
BrgyName text not null,
Unique (fname,mname,lname),
Primary Key (cid));

create table tblcustomertransaction(
services text not null,
primary key (services));

create table tbltransaction(
transactcode serial not null,
Petsa date not null,
cid serial not null,
cdCode serial not null,
borrowedDisc int not null,
rentAmount money not null,
services text not null,
foreign key (services) references tblcustomertransaction (services),
foreign key (cid) references tblcustomer (cid),
foreign key (cdCode) references tblCDetail(cdCode),
Primary key (transactcode,cid,cdCode));


create table tblCDonRent(cid serial not null, 
Petsa date not null,
cdCode serial not null,
Primary key (cid,cdCode),
foreign key (cid) references tblcustomer (cid),
foreign key (cdCode) references tblCDetail(cdCode));

create table tblCDreturned(
Petsa date not null,
cid serial not null,
cdCode serial not null,
transactcode serial not null,
foreign key (cid,cdCode,transactcode) references tbltransaction(cid,cdCode,transactcode), 
primary key (cid,cdCode,transactcode));


create or replace function UpdateAvailability()
Returns Trigger as
$Body$
Begin
if (new.services='rent') then update tblCDetail set availability=availability-new.borrowedDisc
where cdCode=new.cdCode;
insert into tblcdonrent (petsa,cid,cdCode) values (now()::date,new.cid,new.cdCode);
return new;
else
insert into tblcdreturned (petsa,cid,cdCode,transactcode) values (now()::date, new.cid,new.cdCode,new.transactcode);
update tblCDetail set availability=availability+new.borrowedDisc where cdCode=new.cdCode;
delete from tblcdonrent where cid=new.cid and cdCode=new.cdCode; 
return new;
end if;
end;
$Body$ language 'plpgsql' volatile cost 100; 
Alter Function UpdateAvailability()owner to postgres;

create trigger updateAvailability
after insert on tbltransaction
for each row execute procedure UpdateAvailability();

insert into tblCat (genre) values ('action');
insert into tblCat (genre) values ('drama');
insert into tblCat (genre) values ('comedy');
insert into tblCat (genre) values ('musical');


insert into tblCDetail (MovieTitle,gencode,copyright,availability,petsa,rentfee) values ('Iron Man',1,2011,10,now()::date,'25');
insert into tblCDetail (MovieTitle,gencode,copyright,availability,petsa,rentfee) values ('Notebook',2,2012,10,now()::date,'25');
insert into tblCDetail (MovieTitle,gencode,copyright,availability,petsa,rentfee) values ('Babylon Five',1,2013,10,now()::date,'25');
insert into tblCDetail (MovieTitle,gencode,copyright,availability,petsa,rentfee) values ('High School Musical',4,2000,10,now()::date,'25');
insert into tblCDetail (MovieTitle,gencode,copyright,availability,petsa,rentfee) values ('Pidol',3,1990,20,now()::date,'25');


insert into tblcustomer (fname,mname,lname,Street,Purok,BrgyName) values ('Adonis','Balboa','Pilongo','Sanson','Lemonsito','Lumbia');
insert into tblcustomer (fname,mname,lname,Street,Purok,BrgyName) values ('Edilmer','C','Balbutin','?','?','Lleninza');


insert into tblcustomertransaction (services) values ('rent'),('returned');


insert into tbltransaction(petsa,cid,cdcode,borrowedDisc,rentAmount,services) values (now()::date,'1','1','2','50','rent');
insert into tbltransaction(petsa,cid,cdcode,borrowedDisc,rentAmount,services) values (now()::date,'2','1','2','50','rent');
insert into tbltransaction(petsa,cid,cdcode,borrowedDisc,rentAmount,services) values (now()::date,'1','2','4','100','rent');
insert into tbltransaction(petsa,cid,cdcode,borrowedDisc,rentAmount,services) values (now()::date,'1','4','1','1','rent');
insert into tbltransaction(petsa,cid,cdcode,borrowedDisc,rentAmount,services) values (now()::date,'2','3','2','150','rent');
