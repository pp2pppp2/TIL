<template>
  <div>
    <input v-on:change="onInput" type="text">
  </div>
</template>

<script>
//1. 트리거 input 값 변경(@input)
// - 인자: event(e)
// - 실행함수 :onInput

//2. 트리거 input 내 $emit(inputChage)
// - 인자 : 변경된 input 값(inputValue)
// - 실행 함수 onInputChange
export default {
  name: 'SearchBar',
  methods:{
    onInput(e){
      // console.log(e)
      this.$emit('inputChange', e.target.value)
    }
  }
}
</script>

<style scoped>
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>