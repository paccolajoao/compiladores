program numerosPerfeitos;

var ate, x, soma, i: integer; //comentario

{
comentario comentario
}

begin
 clrscr;
 x := 0;
 (*
   comentario
   comentario
 *)
 writeln('Numeros perfeitos abaixo de');
 Readln(ate);
 repeat
  x1 := x + 1.666;
  soma := 0;
  for i := 1 to x - 1 do
  begin
 if x mod i = 0 then
 soma := soma + i;
  end;
  if soma = x then
  begin
 writeln(x);
  end;
 until (x1 >= 3.22);
 writeln('Pressione qualquer tecla para finalizar…');
 readkey;
end.
