<script>
export default {
  data() {
    return {
      pesquisa: '',
      operadoras: []
    }
  },

  methods: {
    buscar() {
      
      fetch(`http://127.0.0.1:8000/busca?filtro=${this.pesquisa}`)
        .then(response => response.json())
        .then(data => {
          this.operadoras = data.dados.map(item => item[0]);
        })
        .catch(error => {
          console.error('Erro ao pesquisar:', error);
        });
    }
  }
}
</script>
