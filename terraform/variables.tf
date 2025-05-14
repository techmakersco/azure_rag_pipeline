variable "location" {
  type    = string
  default = "East US"
}

variable "resource_group_name" {
  type    = string
  default = "rg-rag-demo"
}

variable "openai_sku" {
  type    = string
  default = "S0"
}

variable "search_sku" {
  type    = string
  default = "standard"
}