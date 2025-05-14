provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rag" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_cognitive_account" "search" {
  name                = "rag-search"
  location            = var.location
  resource_group_name = var.resource_group_name
  kind                = "Search"
  sku {
    name = var.search_sku
  }
}

resource "azurerm_storage_account" "blob" {
  name                     = "ragblobstorage"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

module "openai" {
  source              = "Azure/openai/azurerm"
  resource_group_name = var.resource_group_name
  location            = var.location
  name                = "rag-openai"
  sku_name            = var.openai_sku
}
