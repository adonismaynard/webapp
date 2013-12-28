create table tblCat(gencode serial not null, 
genre text not null, 
primary key (gencode));

create table tblCDetail(cdCode serial not null, 
MovieTitle text not null, 
gencode serial not null, 
availability int not null, 
Primary key (cdCode),
Unique (MovieTitle),
foreign key (gencode) references tblCat(gencode));

create table tblcustomer(
cid serial not null,
fname text not null,
lname text null,
mname text not null,
Street text not null,
Purok text not null,
BrgyName text not null,
Unique (fname,lname,mname),
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
insert into tblcdonrent (cid,cdCode) values (new.cid,new.cdCode);
else
insert into tblcdreturned (petsa,cid,cdCode,transactcode) values (now()::date, new.cid,new.cdCode,new.transactcode);
return new;
end if;
end;
$Body$ language 'plpgsql' volatile cost 100; 
Alter Function UpdateAvailability()owner to postgres;

create trigger updateAvailability
after insert on tbltransaction
for each row execute procedure UpdateAvailability();
