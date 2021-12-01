function chunksSliding(row, limit){

   
          
    const prevButName='pb'+row;
    const nextButName='nb'+row;
    
if(limit==1){
$('#'+prevButName).hide();
}else{   
  let textForId='text'+row+'.';
    
let objectArray=[];
    
for(let n=1; n<=limit; n++){
      
      
let slideId=textForId+n;
 let currentSlide=document.getElementById(slideId);
 objectArray.splice(n-1, 0, currentSlide);
  console.log(objectArray)
    
    
    
    };
    
   
    let index=0;
    $('#'+prevButName).on('click', ()=>{
    
      
      let currentSlide=objectArray[index];
        $(currentSlide).hide();
    
        let newIndex=objectArray.indexOf(currentSlide)+1;
        
    
        let newSlide=objectArray[newIndex];
        $(newSlide).show();
     
        if (newIndex>0){
            $('#'+nextButName).show();
        };
        index+=1;
        if (newIndex===(limit-1)){
          $('#'+prevButName).hide();
        }
        
    
    
    });
    
    
    
    $('#'+nextButName).on('click', ()=>{
    
      
      let currentSlide=objectArray[index];
        $(currentSlide).hide();
    
        let newIndex=objectArray.indexOf(currentSlide)-1;
        
    
        let newSlide=objectArray[newIndex];
        $(newSlide).show();
     
        if (newIndex<limit){
            $('#'+prevButName).show();
        };
        index-=1;
        if (newIndex===0){
          $('#'+nextButName).hide();
        }
        
 
    
    });
};
    };

    chunksSliding(1, 3);
        chunksSliding(2, 3);
        chunksSliding(3, 2);
        chunksSliding(4, 2);
            chunksSliding(5, 3);
        chunksSliding(6, 3);
        chunksSliding(7, 3);
        chunksSliding(8, 2);
     chunksSliding(9, 2);
        chunksSliding(10, 2);


