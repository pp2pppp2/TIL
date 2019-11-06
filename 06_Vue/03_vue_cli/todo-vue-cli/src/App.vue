<template>
  <div>
    <h1>여기는 최 상 위컴포 넌 트 입니.</h1>
    <TodoList category="취준"></TodoList>
    <TodoList category="SSAFY"></TodoList>
    <TodoList category="기타"></TodoList>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'

export default{
  components: {
    TodoList,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
