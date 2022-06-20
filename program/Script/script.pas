var
  sHello: string;

procedure HelloWorld (s: string);
begin
  ShowMessage(s);
end;

begin
  // just for example
  sHello := 'Script said hello!';
  HelloWorld(sHello);
end.
