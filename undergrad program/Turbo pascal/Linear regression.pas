{$N+}
{Comentariul 1}
uses crt,graph;
const n=30;
type 
 real = extended;
 vec = array[1..n+1] of real;
 mat = array[1..n+1, 1..n+1] of real;
 
 var iquit				: boolean;
	 i, j,k				: integer;
	 grdriver,grmode	: integer;
	 errcode, gmax,gc	: integer;
	 ipx, ipy, ipy1		: integer;
	 max,min,may,miy,mix	: real;
	 scx,scy,x1,y1		: real;
	 factor,temp,y		: real;
	 an,ani				: real;
	 si,sii,ssi,ssii	: string;
	 a,ainv,aa			: mat;
	 anorm,anormi		: vec;
	 x,b,xx,yy			: vec;
	 

procedure beep;
 begin
  sound(200);delay(220);
  NoSound;
 End;
 
 {**************Modelul pentru Regresia multipla *****************}
 
 procedure model(x:real; var vx:vec);
 var i:integer;
  begin 
  vx[1]:=1;
  vx[2]:=x;
  for i:=2 to gc do
  {------------------------OBSERVATIE ----------------}
  {Relatia intre variabilele regresiei, acuma de tip polinomial,}
  {altfel constand, tipic, din atribuiri independente 			}
  {----------------------------------------------------------}
  vx[i+1]:=vx[i]*x;
  END;
  
{****************** procedura pentru calcul plotare ******************}
function polinom(x:real;b:vec;gmax:integer):real;
var i:integer;
	y,xx:real;
begin                                                                            
y:=b[1];
xx:=1;
for i:=2 to gmax do
 begin
  xx:=xx * x;
 y:=y+b[i] * xx;
 end;
 polinom:=y;
 End;
  
 {*** PROCEDURA PENTRU CALCULUL SUMELOR DIN SISTEMUL LINIAR ****}
  
 procedure sume(x,y:real;var a:mat;var b:vec);
 var j,m	:integer;
     vx		:vec;
 begin
 model(x,vx);
  for m:=1 to gc do 
   begin
   for j:=m to gc+1 do 
		begin
		 a[m,j]:=a[m,j] + vx[j]*vx[m];
		 a[j,m]:=a[m,j];
		 end;
	b[m]:=b[m]+vx[m]*y;
    end;	
END;	
   
   
procedure kaletski(n:integer; var a:mat;
					var b,x,anorm:vec);

var i, j, k, is, l, it :integer;
	s,t,fac:real;
Begin
 b[1]:=b[1]/a[1,1];	
 for j:=2 to n do 
   begin
   a[1,j]:=a[1,j]/a[1,1];
    for i:=2 to n do 
	    begin
		if j>i then begin
		 a[i,j]:=a[j,i]/a[i,i]
		 end else begin
		 s:=0;
		 for k:=1 to j-1 do s:=s+a[i,k]*a[k,j];
		 a[i,j]:=(a[i,j]-s);
			end;
		     end;
	s:=0;
for k:=1 to j-1 do s:=s+a[j,k]*b[k];
		b[j]:=(b[j]-s)/a[j,j];
		end;
end;	



{*****CONSTRUIREA SOLUTILOR SISTEMULUI LINIAR ****}

procedure solutii(n:integer;a:mat;b:vec;var x:vec);
var t:real;
    i:integer;
Begin
 x[n]:=b[n];
 for i:=n-1 downto 1 do begin
t:=0;
 for j:=i+1 to n do t:=t+a[i,j]*x[j];
   x[i]:=b[i]-t;
  end;
End;	

procedure matinvk(a:mat;n:integer;var ainv:mat);
var ii,i,j,k :integer;
 b,x 	     :vec;
 s,t	     :real;
begin

for ii:=1 to n do
 begin 
  for j:=1 to n do b[j]:=0;
  b[ii]:=1;
  
  b[1]:=b[1]/a[1,1];
  for j:=2 to n do 
  begin 
  s:=0;
   for k:=1 to j-1 do s:=s+a[j,k]*b[k];
   b[j]:=(b[j]-s)/a[j,j];
   end;
   
   ainv[n,ii]:=b[n];
   for i:=n-1 downto 1 do 
    begin
     t:=0;
	 for j:=i+1 to n do 
	  t:=t+a[i,j]*ainv[j,ii];
	  ainv[i,ii]:=(b[i]-t);
	end;
end;
End;
   

{************************************************************************************}
{*********************************** PRINCIPAL ***********************************}
{*************************************************************************************}
Begin
randomize;
clrscr;
iquit:=true;
repeat 
write('Gradul maxim al regresiei = ');
readln(gmax);
if gmax>n-1 then begin
 clrscr;
 beep;
 highvideo;
 gotoxy(1,1);
 writeln('Gradul maxim admins este: ', (n-1):2);
 lowvideo;
 end;
 until gmax <=n;
 
 gmax:=gmax+1;
 write('Factorul de eroare ');
 readln(factor);
 factor:=factor*2.0;
 clrscr;
 gotoxy(10,12);
 writeln('Programul este in executie Normala ');
 for i:=1 to gmax+1 do 
  begin
   for j:=1 to gmax+1 do 
    a[i,j]:=0;
	x[i]:=0;
	end;

{Generam un polinom afectat de erori "exeprimentale"	}
for i:=1 to n do 
 begin
 x1:=i;
 y1:=sqr(x1);
 y1:=-12*3*x1-30*y1+2*x1*y1;
 xx[i]:=x1;{vectorul necesar pentru grafic }
 yy[i]:=(y1+factor*(random-0.5)*sqrt(abs(y1)));
 end;{!!!!!!!!!!!!}
 {Pregatim sistemul de eciatoo pt.regresie robusta }
 gc:=gmax;
  for i:=1 to n do sume(xx[i],yy[i],a,x);
 kaletski(gmax,a,x,b,anorm);
 matinvk(a,gmax,ainv);
 an:=0;
 for k:=1 to gmax do
  begin
   anorm[k]:=0;
   anormi[k]:=0;
   for i:=1 to k do 
    begin
    for j:=1 to k do 
     begin 	
	  anorm[k]:=anorm[k]+sqr(a[i,j]);
	  anormi[k]:=anormi[k]+sqr(ainv[i,j]);
	  end;
	end;  
end;

{Inceputul regresie robusta }
i:=detect;
initgraph(i,i,'..\bgi');
errcode:=graphresult;
if errcode=grOK then 
 begin
 ClearDevice;
{ cleardeivce;}
 max:=xx[1];
 mix:=xx[1];
 may:=yy[1];
 miy:=yy[1];
 for i:=1 to n do 
  begin
  if yy[i]<miy then miy:=yy[i];
  if yy[i]>may then may:=yy[i];
  if xx[i]<mix then  mix:=xx[i];
  if xx[i] > max then max:=xx[i];
  end;
  
  scx:=400/(max-min);
  scy:=200/(may-mix);
  
  for i:=1 to n do {semnul "+" pt.datele experim. }
   begin 
    line(200+round(scx*(xx[i]-mix)+4), 
	     250-round(scy*(yy[i]-miy)), 
		 round(200+scx*(xx[i]-mix)-4),
		 250-round(scy*(yy[i]-miy)));
	line(round(200+scx*(xx[i]-mix)),
	     246-round(scy*(yy[i]-miy)), 
		 round(200+scx*(xx[i]-mix)),
		 254-round(scy*(yy[i]-miy)));
	end;
	str((gmax-1):2,si);
	outtextxy(0,320,'Gradul maxim al polinomului de regresie = '+si);
	str((factor/2):5:3,ssi);
	outtextxy(0,310,'Factorul de eroare este= '+ssi);
	iquit:=true;
	while iquit do
	begin
	 setviewport(0,0,185,260,false);
	 clearviewport;
	 
	 repeat
	 textcolor(6);
	 outtextxy(0,10,'Grd.actual al regresie= ? ');
	 gotoxy(120,1);
	 readln(gc);
	 gc:=gc+1;
	 str(gc:2,sii);
	 if gc > gmax then begin
	  beep;
	  clearviewport;
	  outtextxy(0,0,'Gresit! Grd.max.= '+si);
	end;
until	gc <=gmax;
an:=0;{calculam numarul de coditionare }
ani:=0; {al matricii sist.lin.pt grad gc. }
for i:=1 to gc do 
 begin
 an:=an+anorm[i];
 ani:=ani+anormi[i];
 end;
 
 an:=sqrt(an);{norma matricii a}
 ani:=sqrt(ani);{norma matricii ain}
 clearviewport;
 solutii(gc,a,x,b);
 outtextxy(1,15,'Coeficientii: ');
 for i:=1 to gc do 
  begin
   str((i-1):2,sii);
   str(b[i]:9:3,ssi);
   outtextxy(1,20+10*i,'a('+sii+')='+ssi);
   end;
str((an*ani):9,ssi);   
outtextxy(0,250,'Nr.cond.= '+ssi);
moveto(200,250);
y1:=polinom(mix,b,gc);
ipx:=1;
ipy:=250-round(scy*(y1-miy));
ipy1:=ipy;
moveto(200,ipy);
for i:=2 to 400 do 
 begin
 x1:=(i-1)/scx+mix;
 y1:=polinom(x1,b,gc);
 ipy:=250-round(scy*(y1-miy));
 if(ipy<0) or (ipy>270) then 
  begin
  if ipy<0 then ipy1:=10 else ipy1:=270;
  ipx:=i; {punctul iesit din scala }
  moveto(200+i,ipy);
  end else 
  lineto(200+i,ipy);
  end;
outtextxy(200+ipx,ipy1+8,sii);
outtextxy(0,290,'Apasa <ENTER> pentru a continua regresia');
outtextxy(0,300,'Sau orice alta tasta pentru a terminare. ');
readln(si);
if si<>'' then iquit:=false;
clearviewport;
  end;{end if grafic }
 end;
closegraph;
END. 


	 
	
	




















		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
	
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
					
					





















   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
	 