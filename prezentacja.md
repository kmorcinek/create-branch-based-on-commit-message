
&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## Chcesz poprosić o Code Review (bo musisz?) i robisz Pull Request/Merge Request

<!---
albo po prostu masz taki flow
--->

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<!---
opowiem jak to u mnie wygladalo
--->

```bash
git commit -am "extend endpoint with finalImage property"
```

```git
git checkout -b final-image-endpoint-extension
```

sparafrazowac (jakby w innej formie).

&nbsp;

&nbsp;

&nbsp;

&nbsp;

```bash
git commit -am "#WW-1024 extend endpoint with finalImage property"
```

```bash
git checkout -b feat/1024/final-image-endpoint-extension
```

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## (wymyślanie tych nazw zaczęło mnie nużyć...)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

`feat/WW-1024/extend-endpoint-with-final-image-property`

cały &nbsp; ^ ticket z np Jiry

`refactor/WW-1084/use-type-net-quantity-instead-of-decimal`

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<!---
Mowimy tu o sytuacji gdy chce poprosic o CR. 
--->
## IMHO feature powinien się składać z serii kroków dla lepszej czytelności i poprawy istniejącego kodu

&nbsp;

1. extend "something"
&nbsp;

&nbsp;

2. fix "something"
&nbsp;

&nbsp;

3. "refactoring" before final step
&nbsp;

&nbsp;

4. feat: #WW-1024 extend endpoint with finalImage property

&nbsp;

&nbsp;

`feat/WW-1024/extend-endpoint-with-final-image-property`

[//]: # "^ w filmie scroluje na dół"
[//]: # "^ i z tego ostatniego bedzie PR/MR"

&nbsp;

&nbsp;

&nbsp;

&nbsp;

## Automat robi za mnie

| Commit message | | Branch name |
| ----------- | ----------- | ----------- |
| `"feat: #OLDM-324 create product endpoint"` | &rarr; | `"feat/OLDM-324/create-product-endpoint"` |
| `"fix: fix email"` | &rarr; | `"fix/fix-email"` |
| `"add new TODO"` | &rarr; | `"add-new-todo"` |

<!---
w kolejnym filmie pokaze prosty skrypt ktory robi ta robote.

TODO lista kilku convencji :
  origin/chore/dev_jvm_params
  origin/chore/upgrade-parent-pom-version
  origin/feat/CreateInMemoryCachesForProductCatalog
  origin/feat/OLDM-1155/GetListOfTheKitchensFromErp
  origin/feat/define-product-wip
  origin/fix/CacheKeyAlsoByBrandId
  origin/fix/ChangeFetchingBrandsOneByOne
  origin/fix/ChangeProductCatalogCacheToRedisCache
  origin/fix/IncreaseMemoryInWebClient
  origin/fix/OLDM-1108/validate-request-filters-in-product-catalogproducts-endpoint
  origin/fix/OLDM-1198/remove-duplicated-fpds-from-product-catalog-response
  origin/fix/OLDM-761/ExportRecipeDefinitionShouldNotContainsKob
--->
