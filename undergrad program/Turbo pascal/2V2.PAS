uses crt,graph;

{ programa dată desenează o rachetă în regimi grafic și permite setarea direcției de navigare în timp real.
}
var
  cuposX,cuposY:integer;
  p,back,left,right:pointer;
  size:word;


procedure initiere;
var gd,gm:integer;
    errCode:integer;
begin
 gd:=detect;
 initGraph(gd,gm,'..\bgi');
 if errcode<>grOk then writeln('graphics error: ',GraphErrorMsg(ErrCode));
end;


procedure drawRacket;
begin
rectangle(10, 20, 45,130);
{10,20,45,160}
moveTo(10, 20);
lineTo(25, 10);
lineTo(45, 20);{45,20}
end;

procedure drawWithback;
begin
rectangle(10, 20, 45,130);
{10,20,45,130}
moveTo(10, 130);{10, 20}
lineTo(25, 160);{25,10}{virfu}
lineTo(45, 130);{45,20}
end;{merge OK, save aceleasi parametri}


procedure drawRacketDreapta;
begin
rectangle(10, 20, 160,45);
{10,20,45,160}
moveTo(160, 45);{10,20}
lineTo(175, 30);{25,10}
lineTo(160, 20);{45,20}
end;

procedure drawLeft;
begin
rectangle(20, 20, 160,45);{20,20,160,45}
{10,20,45,160}
moveTo(20, 45);{10,20}
lineTo(5, 30);{25,10}
lineTo(20, 20);{45,20}
{rectangle(10, 20, 45,160);
{10,20,45,160}
{moveTo(10, 20);{10,20}
{lineTo(25, 10);{25,10}
{lineTo(45, 20);{45,20}
end;

procedure save(x:integer;y:integer;c:char);
var a:pointer;
begin
size:=ImageSize(0,0,x,y);
{50,200,450,400}
getMem(a,size);
getImage(0,0,x,y,a^);
case c of
'p':p:=a;
'1':back:=a;
'3':left:=a;
'2':right:=a;
end;
end;





procedure movdx(dx:integer;dy:integer;a:pointer);
var x,y:word;
begin
cleardevice;
x:=cuposX+dx;
y:=cuposY+dy;
if((x>0) and (x<getMaxX-180)and(y>0)and(y<getmaxY-130)) then begin
    putImage(x,y,a^,normalPut);
    cuposX:=x;
    cuposY:=y;
 end;
end;




procedure initiereObiecte;
begin
drawRacket;
save(45,400,'p');
cleardevice;

drawWithback;
save(45,400,'1');
cleardevice;

drawRacketDreapta;
save(175,45,'2');{sageata In jos}
cleardevice;

drawLeft;
save(160,45,'3');
cleardevice;
{saveHorisontal;}
end;



procedure miscare;
var stop:boolean;
     x,y:integer;
    const d=10;
begin
stop:=false;
repeat
 case readkey of
 {#71 : movdx(-d,-d);}
 #72 : movdx(0,-d,p);
{ #73 : movdx(d,-d);}
 #75 : movdx(-d,0,left);
 #77 : movdx(d,0,right);
 {#79 : movdx(-d,d);}
 #80 : movdx(0,d,back);
 {#81 : movdx(d,d);}
 #27 : stop:=true;

 end;
 until stop
 end;


Begin
initiere;
cuposX:=getmaxX div 2;
cuposY:=getmaxY div 2;

initiereObiecte;
OutText('Tastati sageata ');
miscare;

readkey;
closeGraph;
end.


