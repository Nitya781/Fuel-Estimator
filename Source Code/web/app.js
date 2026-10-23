async function updateFuelData() {

    try {

        const response = await fetch("http://localhost:8001/api");
        const data = await response.json();


        document.getElementById("fuel").innerHTML =
            data.fuel_remaining + " kg";

        document.getElementById("flow").innerHTML =
            data.fuel_flow + " kg/hr";

        document.getElementById("sfc").innerHTML =
            data.sfc;


        document.getElementById("endurance").innerHTML =
            data.endurance + " hr";

        document.getElementById("range").innerHTML =
            data.range + " NM";

        document.getElementById("landing").innerHTML =
            data.fuel_landing + " kg";


        document.getElementById("reserve").innerHTML =
            data.reserve + " kg";

        document.getElementById("bingo").innerHTML =
            data.bingo + " kg";


        document.getElementById("status").innerHTML =
            data.status;


    }

    catch(error) {

        console.log("Waiting for API connection...");
    }

}


// Update every 5 seconds
setInterval(updateFuelData, 5000);


// First update immediately
updateFuelData();
