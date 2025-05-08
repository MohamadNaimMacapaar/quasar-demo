<template>
  <q-layout view="hHh lpR fFf">

    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar.png">
          </q-avatar>
          CICS Thesis Archive
        </q-toolbar-title>
        <q-input
          outlined
          dense
          placeholder="Search..."
          v-model="searchQuery"
          class="q-ml-md bg-white"
          clearable
          @input="onSearch"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" elevated>
      <q-list>
        <q-item clickable v-ripple @click="onButtonClick('dashboard')">
          <q-item-section avatar>
            <q-icon name="dashboard" />
          </q-item-section>
          <q-item-section>
            Dashboard
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple @click="onButtonClick('register')">
          <q-item-section avatar>
            <q-icon name="assignment_ind" />
          </q-item-section>
          <q-item-section>
            Register Thesis
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple @click="onButtonClick('manage')">
          <q-item-section avatar>
            <q-icon name="assignment" />
          </q-item-section>
          <q-item-section>
            Manage Thesis
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple @click="onButtonClick('history')">
          <q-item-section avatar>
            <q-icon name="history" />
          </q-item-section>
          <q-item-section>
            Logs
          </q-item-section>
        </q-item>

        <q-item clickable v-ripple @click="onButtonClick('settings')">
          <q-item-section avatar>
            <q-icon name="settings" />
          </q-item-section>
          <q-item-section>
            Settings
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const leftDrawerOpen = ref(false)

    const toggleLeftDrawer = () => {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }

    const onButtonClick = (buttonName) => {
      console.log(`${buttonName} button clicked`)
      // Add your navigation or logic here
    }

    return {
      leftDrawerOpen,
      toggleLeftDrawer,
      onButtonClick
    }
  }
}
</script>
