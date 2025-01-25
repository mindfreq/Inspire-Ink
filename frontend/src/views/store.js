import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    formData: {}
  },
  mutations: {
    updateFormData(state, payload) {
      state.formData = { ...state.formData, ...payload };
    }
  },
  actions: {
    updateFormData({ commit }, payload) {
      commit('updateFormData', payload);
    }
  }
});