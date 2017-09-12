program intrebari;
uses crt,graph;
{label:1(table);}
type intrebare = record
	subiect : string;
	Ra, Rb, Rc, Rd, Corect:string[28];
	end;
var a:array[1..100] of intrebare;
    f:text;
    f1:file of intrebare;
    i,j,n,k,punctaj:byte;
    s:set of byte;
    c:char;
    r:string[28];
    sel:integer;
    Rc,Ri:array[1..10] of integer;
    nume, key,Tkey,strlen:string;
    




procedure initiere;
begin
 tkey:='';
 write('scrie numele tau ');
 readln(nume);
 for i:=1 to length(nume) do tkey:=nume[i]+tkey;
 if ( nume='' ) then
  begin
   gotoXY(getMaxX div 2,getMaxy div 2);
   write('Nu ati scris numele corect! La revedere!');
   writeln(readkey);
   exit;
  end;
 Randomize;
end;  


procedure citire;
begin
 assign(f,'subiecte.txt');
 assign(f1,'sub1.in');
 reset(f);
 rewrite(f1);
 i:=0;
 while not(eof(f)) do
  begin
   inc(i);
   with a[i] do
    begin
     readln(f,subiect);	
     readln(f,Ra);
     readln(f,Rb);
     readln(f,Rc);
     readln(f,Rd);
     readln(f,corect);
     end;
     write(f1,a[i]);
   end;
   n:=i;
   write('A fost citite ',i, 'intrebari');
   close(F);
   close(f1);
   writeln(n);
end;     


procedure schimbareaCulori;
begin
textcolor(14);
textbackground(4);
end;

procedure culoareNormala;
begin
 textcolor(0);
 textbackground(15);
end; 


procedure afisareaIntrebari;
begin
 assign(f1,'sub1.in');
 reset(f1);
 randomize;
 
 punctaj:=0;
 s:=[];
 j:=0;
WRITELN('SPATIU ESTE ECHIVALENT CU ENTER ');
 while ( true ) do
  begin
   inc(j);
   k:=random(n) + 1;
   if (k = 0) then i:=n else  i:=k-1;
   while(( k in s )and( k<>i )) do
    begin
     inc(k);
     if (k = n) then k:=1;
    end;

    if not(k in s) then begin
     s:=s + [k];
     seek(f1,k-1);
     read(f1,a[k]);
     clrscr;
     write(i,'.');
     with a[k] do begin
     clrscr;
     sel:=1;
     writeln(j, '; ', a[k].subiect);
     writeln('a. ',a[k].Ra);
     writeln('b. ',a[k].Rb);
     writeln('c. ',a[k].Rc);
     writeln('d. ',a[k].Rd);
     writeln('Apasa ESC pentru a iesi..');

     repeat
      c:=readkey;
      case c of 
      #72: begin sel:=sel-1; if( sel <1 ) then sel:=4; end;
      #80: begin sel:=sel + 1; if( sel >4 ) then sel:=1; end;
      #27: begin
           clrscr;
           writeln(nume,' ai acumulat ',punctaj, ' de puncte!');
           writeln('Tastati Enter! ');
           readln;
           close(F1);
           exit;
           end;
        end;       
    clrscr;
    writeln(j,'. ',a[k].subiect);
    if( sel = 1 )then
     begin
     schimbareaCulori;
      writeln('a.',a[k].Ra);
      culoareNormala;
      end else 
      begin
       writeln('a.',Ra);
      end;
      if( sel = 2) then
       begin
        schimbareaCulori;
        writeln('b.',Rb);
        culoareNormala;
       end else 
        begin
         writeln('b.',Rb);
        end;

        if(sel = 3) then 
        begin 
         schimbareaCulori;
         writeln('c.',Rc);
         culoareNormala;
         end else 
         begin 
          writeln('d.',Rc);
         end;
        if(sel = 4)  then 
        begin
        schimbareaCulori;
        writeln('d.',Rd);
        culoareNormala;
        end else
        begin
        writeln('d.',Rd);
        end;
        writeln('Apasa ESC pentru a iesi....');
        until c=#32;
        case sel of 
        1:r:=Ra;
        2:r:=Rb;
        3:r:=Rc;
        4:r:=Rd;
        end;
        clrscr;
        if ( r = corect ) then begin
         writeln('Corect! ');
         inc(punctaj);
         delay(200);

         end else 
         begin
         writeln('Incorect !');
         writeln('Apasa orice tasta ');
         readkey;
         end;
      end;
    end;
end;


clrscr;
writeln(nume,' ai acumulat ',punctaj,' puncte');
writeln('Apasa Enter');
readkey;
close(f1);
end;


Begin
 clrscr;
 initiere;
 citire;
 afisareaIntrebari;
end.



 
 