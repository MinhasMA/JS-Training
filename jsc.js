//var x = 8
//console.log(x)

var colour = 'amber'
console.log(colour)
switch (colour)
{
    case 'red':
    case 'amber':
         stop();
         break;
    case 'green':
    case 'flashing amber':
         go();
         break;
    default:
         throw 'Invalid colour';
}