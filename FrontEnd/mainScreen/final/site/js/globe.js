document.addEventListener('DOMContentLoaded', function() {
  const WORLD_IMAGE_URL = '//unpkg.com/three-globe/example/img/earth-dark.jpg';
  const GEOJSON_PATH = '../datasets/updated_world.geojson';
  
  const world = Globe()(document.getElementById('globe'));

  world
    .globeImageUrl(WORLD_IMAGE_URL)
    .pointOfView({ altitude: 2 }, 1000)
    .polygonCapColor(() => 'rgba(255, 255, 255, 1)') // Set all countries to white
    .polygonSideColor(() => 'rgba(255, 255, 255, 0.3)') // Optional: semi-transparent side color
    .polygonStrokeColor(() => 'rgba(0, 0, 0, 1)')
    .atmosphereColor("#ffffff")
    .backgroundColor("#f9f9f9")
    .width(600)
    .height(500);

  world.controls().autoRotate = true;
  world.controls().autoRotateSpeed = 0.75;

  fetch(GEOJSON_PATH)
    .then(res => res.json())
    .then(countries => {
      world.polygonsData(countries.features.filter(d => d.properties.ISO_A2 !== 'AQ'));
    })
    .catch(err => console.error("Failed to fetch GeoJSON data:", err));
});