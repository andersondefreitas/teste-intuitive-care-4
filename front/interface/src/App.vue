<template>
  <div>
    <!-- Campo de pesquisa -->
    <input type="text" v-model="pesquisa" placeholder="Digite sua pesquisa..." />

    
    <button class="btn" @click="buscar">Pesquisar</button>

    
    <ul>
      <li v-for="(operadora, index) in operadoras" :key="index">
        {{ operadora }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pesquisa: '', 
      operadoras: [] 
    };
  },

  methods: {
    buscar() {
      fetch(`http://127.0.0.1:8000/busca?filtro=${this.pesquisa}`)
        .then(response => response.json())
        .then(data => {
          
          if (data.resultados && data.resultados.length > 0) {
            this.operadoras = data.resultados[0].registros; 
          }
        })
        .catch(error => {
          console.error('Erro ao pesquisar:', error);
        });
    }
  }
}
</script>
